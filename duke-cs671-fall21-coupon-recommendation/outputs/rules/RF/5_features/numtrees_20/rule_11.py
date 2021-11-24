def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[3]<=1.0:
		# {"feature": "Occupation", "instances": 33, "metric_value": 0.994, "depth": 2}
		if obj[2]<=17:
			# {"feature": "Distance", "instances": 30, "metric_value": 1.0, "depth": 3}
			if obj[4]>1:
				# {"feature": "Education", "instances": 19, "metric_value": 0.9819, "depth": 4}
				if obj[1]>0:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[0]>2:
						return 'True'
					elif obj[0]<=2:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]<=1:
				# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[1]>1:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]>2:
						return 'True'
					elif obj[0]<=2:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>17:
			return 'False'
		else: return 'False'
	elif obj[3]>1.0:
		# {"feature": "Distance", "instances": 18, "metric_value": 0.7642, "depth": 2}
		if obj[4]>1:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[2]>2:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[0]<=3:
					# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>3:
					return 'True'
				else: return 'True'
			elif obj[2]<=2:
				return 'False'
			else: return 'False'
		elif obj[4]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'
