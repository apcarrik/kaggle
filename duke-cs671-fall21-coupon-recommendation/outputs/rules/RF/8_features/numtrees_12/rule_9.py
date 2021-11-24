def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9465, "depth": 1}
	if obj[7]<=2:
		# {"feature": "Bar", "instances": 75, "metric_value": 0.9044, "depth": 2}
		if obj[4]<=3.0:
			# {"feature": "Coupon", "instances": 73, "metric_value": 0.883, "depth": 3}
			if obj[1]>0:
				# {"feature": "Restaurant20to50", "instances": 65, "metric_value": 0.8291, "depth": 4}
				if obj[5]<=2.0:
					# {"feature": "Occupation", "instances": 60, "metric_value": 0.86, "depth": 5}
					if obj[3]>0:
						# {"feature": "Passanger", "instances": 56, "metric_value": 0.8856, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Education", "instances": 35, "metric_value": 0.9518, "depth": 7}
							if obj[2]>0:
								# {"feature": "Direction_same", "instances": 26, "metric_value": 0.8905, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[2]<=0:
								# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[0]>1:
							# {"feature": "Education", "instances": 21, "metric_value": 0.7025, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Direction_same", "instances": 19, "metric_value": 0.6292, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]>2:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[5]>2.0:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[2]>0:
					# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[3]>2:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[5]>-1.0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0]>1:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						elif obj[5]<=-1.0:
							return 'False'
						else: return 'False'
					elif obj[3]<=2:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[4]>3.0:
			return 'False'
		else: return 'False'
	elif obj[7]>2:
		# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[2]>0:
			# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[5]<=1.0:
				return 'True'
			elif obj[5]>1.0:
				return 'False'
			else: return 'False'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
