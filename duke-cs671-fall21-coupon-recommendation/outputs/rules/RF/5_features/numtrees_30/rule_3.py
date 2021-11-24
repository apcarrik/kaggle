def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[2]>1:
		# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.9992, "depth": 2}
		if obj[3]<=3.0:
			# {"feature": "Coupon", "instances": 29, "metric_value": 0.9923, "depth": 3}
			if obj[0]<=3:
				# {"feature": "Distance", "instances": 16, "metric_value": 0.9887, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				elif obj[4]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>3:
				# {"feature": "Distance", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[4]<=1:
					# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[4]>1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[3]>3.0:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		return 'True'
	else: return 'True'
