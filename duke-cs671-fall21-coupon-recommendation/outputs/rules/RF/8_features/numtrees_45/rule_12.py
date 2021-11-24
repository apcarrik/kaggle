def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[3]>1:
		# {"feature": "Education", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[2]<=1:
			# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[7]<=2:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[0]>0:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[7]>2:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]>2.0:
				return 'False'
			else: return 'False'
		elif obj[2]>1:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[1]>1:
				return 'False'
			elif obj[1]<=1:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[7]>2:
					return 'False'
				elif obj[7]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[3]<=1:
		return 'True'
	else: return 'True'
