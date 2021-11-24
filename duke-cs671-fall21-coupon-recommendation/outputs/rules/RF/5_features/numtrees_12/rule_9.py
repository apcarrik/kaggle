def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9555, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 65, "metric_value": 0.8905, "depth": 2}
		if obj[2]<=6:
			# {"feature": "Distance", "instances": 35, "metric_value": 0.971, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Education", "instances": 33, "metric_value": 0.9834, "depth": 4}
				if obj[1]>0:
					# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 1.0, "depth": 5}
					if obj[3]>0.0:
						return 'False'
					elif obj[3]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[3]>0.0:
						return 'True'
					elif obj[3]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]>2:
				return 'True'
			else: return 'True'
		elif obj[2]>6:
			# {"feature": "Education", "instances": 30, "metric_value": 0.7219, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.5159, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "Distance", "instances": 23, "metric_value": 0.5586, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[3]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[4]>1:
					return 'False'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Distance", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[3]<=2.0:
				# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[2]<=7:
						return 'False'
					elif obj[2]>7:
						return 'False'
					else: return 'False'
				elif obj[1]>0:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]>6:
						return 'False'
					elif obj[2]<=6:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>2.0:
				return 'True'
			else: return 'True'
		elif obj[4]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
