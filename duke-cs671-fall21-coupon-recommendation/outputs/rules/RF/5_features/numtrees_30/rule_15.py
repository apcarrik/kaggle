def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[2]>1:
		# {"feature": "Distance", "instances": 31, "metric_value": 0.9992, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9923, "depth": 3}
			if obj[3]>-1.0:
				# {"feature": "Education", "instances": 27, "metric_value": 0.999, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Coupon", "instances": 26, "metric_value": 0.9957, "depth": 5}
					if obj[0]<=3:
						return 'True'
					elif obj[0]>3:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[3]<=-1.0:
				return 'True'
			else: return 'True'
		elif obj[4]>2:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		return 'True'
	else: return 'True'
