def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Direction_same", "instances": 13, "metric_value": 0.9612, "depth": 2}
		if obj[9]<=0:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[5]>4:
				return 'False'
			elif obj[5]<=4:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[9]>0:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[7]<=3.0:
			return 'True'
		elif obj[7]>3.0:
			return 'False'
		else: return 'False'
	else: return 'True'
