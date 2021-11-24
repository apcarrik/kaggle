def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coupon", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 12, "metric_value": 1.0, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[4]<=1:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					else: return 'True'
				elif obj[4]>1:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[4]<=2:
					return 'True'
				elif obj[4]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		return 'True'
	else: return 'True'
