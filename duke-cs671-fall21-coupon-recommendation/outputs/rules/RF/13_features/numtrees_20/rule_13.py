def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9183, "depth": 1}
	if obj[2]>1:
		# {"feature": "Passanger", "instances": 37, "metric_value": 0.6998, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Distance", "instances": 19, "metric_value": 0.9495, "depth": 3}
			if obj[12]<=2:
				# {"feature": "Time", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[7]>1:
						# {"feature": "Bar", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[8]>0.0:
							# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=3:
								# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[9]<=1.0:
									return 'True'
								elif obj[9]>1.0:
									# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]<=1:
										# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]>3:
								return 'False'
							else: return 'False'
						elif obj[8]<=0.0:
							# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]>0:
								return 'False'
							elif obj[6]<=0:
								# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]>2:
									return 'False'
								elif obj[4]<=2:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[7]<=1:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[12]>2:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[9]>0.0:
			# {"feature": "Occupation", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[7]>5:
				# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				elif obj[3]>0:
					return 'False'
				else: return 'False'
			elif obj[7]<=5:
				return 'True'
			else: return 'True'
		elif obj[9]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'False'
