def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]<=16:
		# {"feature": "Education", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[3]<=1.0:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[0]<=3:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>3:
					return 'False'
				else: return 'False'
			elif obj[3]>1.0:
				return 'True'
			else: return 'True'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	elif obj[2]>16:
		return 'True'
	else: return 'True'
