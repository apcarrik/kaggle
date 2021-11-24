def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[2]<=12:
		# {"feature": "Coupon", "instances": 30, "metric_value": 0.9183, "depth": 2}
		if obj[0]>1:
			# {"feature": "Distance", "instances": 25, "metric_value": 0.795, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Education", "instances": 21, "metric_value": 0.5917, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[3]>2:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[0]<=1:
			# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[3]<=1:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[3]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]>12:
		return 'False'
	else: return 'False'
