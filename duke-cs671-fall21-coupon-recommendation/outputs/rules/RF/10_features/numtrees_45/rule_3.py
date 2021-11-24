def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]>1:
		# {"feature": "Bar", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[5]<=1.0:
			return 'True'
		elif obj[5]>1.0:
			return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Direction_same", "instances": 11, "metric_value": 0.9457, "depth": 2}
		if obj[8]<=0:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[2]>2:
				return 'False'
			elif obj[2]<=2:
				# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[8]>0:
			return 'True'
		else: return 'True'
	else: return 'False'
