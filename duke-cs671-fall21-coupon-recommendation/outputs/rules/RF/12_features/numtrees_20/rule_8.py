def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[5]>1:
		# {"feature": "Occupation", "instances": 28, "metric_value": 0.9963, "depth": 2}
		if obj[6]<=16:
			# {"feature": "Direction_same", "instances": 26, "metric_value": 0.9829, "depth": 3}
			if obj[10]<=0:
				# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 4}
				if obj[2]>0:
					# {"feature": "Age", "instances": 21, "metric_value": 0.9984, "depth": 5}
					if obj[4]>0:
						# {"feature": "Distance", "instances": 19, "metric_value": 0.9819, "depth": 6}
						if obj[11]>1:
							# {"feature": "Time", "instances": 12, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[8]<=2.0:
									# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[7]<=0.0:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[7]>0.0:
												return 'False'
											else: return 'False'
										elif obj[0]>1:
											return 'False'
										else: return 'False'
									elif obj[9]>1.0:
										return 'True'
									else: return 'True'
								elif obj[8]>2.0:
									return 'True'
								else: return 'True'
							elif obj[1]>2:
								return 'True'
							else: return 'True'
						elif obj[11]<=1:
							# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[7]<=2.0:
								# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[9]>0.0:
									return 'False'
								elif obj[9]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[7]>2.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]<=0:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[10]>0:
				return 'False'
			else: return 'False'
		elif obj[6]>16:
			return 'True'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Distance", "instances": 23, "metric_value": 0.5586, "depth": 2}
		if obj[11]<=2:
			# {"feature": "Age", "instances": 22, "metric_value": 0.4395, "depth": 3}
			if obj[4]>3:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.6194, "depth": 4}
				if obj[6]>4:
					# {"feature": "Gender", "instances": 12, "metric_value": 0.4138, "depth": 5}
					if obj[3]<=0:
						return 'True'
					elif obj[3]>0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>1:
							return 'True'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]<=4:
					return 'False'
				else: return 'False'
			elif obj[4]<=3:
				return 'True'
			else: return 'True'
		elif obj[11]>2:
			return 'False'
		else: return 'False'
	else: return 'True'
