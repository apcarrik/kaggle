def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Occupation", "instances": 36, "metric_value": 0.9911, "depth": 2}
		if obj[2]<=6:
			# {"feature": "Education", "instances": 20, "metric_value": 0.8813, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.8315, "depth": 4}
				if obj[3]<=2.0:
					# {"feature": "Distance", "instances": 16, "metric_value": 0.896, "depth": 5}
					if obj[4]<=1:
						return 'True'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				elif obj[3]>2.0:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[2]>6:
			# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[3]<=1.0:
				# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Distance", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[3]>1.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>3:
		# {"feature": "Occupation", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[2]>2:
			# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[3]>-1.0:
				# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[4]>2:
					return 'False'
				else: return 'False'
			elif obj[3]<=-1.0:
				return 'False'
			else: return 'False'
		elif obj[2]<=2:
			return 'False'
		else: return 'False'
	else: return 'False'
