def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 28, "metric_value": 0.9852, "depth": 2}
		if obj[3]<=11:
			# {"feature": "Passanger", "instances": 20, "metric_value": 0.9928, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[4]>1.0:
						# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[2]<=0:
							return 'True'
						elif obj[2]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[5]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[2]>1:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2:
							return 'False'
						else: return 'False'
					elif obj[4]>1.0:
						return 'False'
					else: return 'False'
				elif obj[2]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>11:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=0:
					return 'True'
				elif obj[2]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
