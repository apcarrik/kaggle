def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[8]<=3.0:
		# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 1.0, "depth": 2}
		if obj[9]>1.0:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[6]>4:
				return 'False'
			elif obj[6]<=4:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[9]<=1.0:
			# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[3]<=0:
				return 'True'
			elif obj[3]>0:
				# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[10]<=0:
					return 'False'
				elif obj[10]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[8]>3.0:
		return 'False'
	else: return 'False'
