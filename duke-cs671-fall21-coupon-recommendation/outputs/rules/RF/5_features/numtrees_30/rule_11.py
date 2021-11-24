def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[4]<=2:
		# {"feature": "Coupon", "instances": 32, "metric_value": 0.9745, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Occupation", "instances": 17, "metric_value": 0.7871, "depth": 3}
			if obj[2]<=6:
				# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[3]>0.0:
						return 'True'
					elif obj[3]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[2]>6:
				return 'True'
			else: return 'True'
		elif obj[0]>3:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[2]<=6:
				# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[3]>0.0:
					return 'True'
				elif obj[3]<=0.0:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=0:
						return 'False'
					elif obj[1]>0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]>6:
				# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[1]<=2:
					return 'False'
				elif obj[1]>2:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					elif obj[3]>1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[4]>2:
		return 'False'
	else: return 'False'
