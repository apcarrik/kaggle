def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9367, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 67, "metric_value": 0.8171, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Occupation", "instances": 46, "metric_value": 0.5586, "depth": 3}
			if obj[7]>1:
				# {"feature": "Coffeehouse", "instances": 36, "metric_value": 0.65, "depth": 4}
				if obj[9]<=2.0:
					# {"feature": "Gender", "instances": 27, "metric_value": 0.7642, "depth": 5}
					if obj[3]>0:
						# {"feature": "Time", "instances": 19, "metric_value": 0.4855, "depth": 6}
						if obj[1]<=3:
							return 'True'
						elif obj[1]>3:
							# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[4]<=3:
								return 'True'
							elif obj[4]>3:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[10]>0.0:
							# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]>0:
									return 'True'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[10]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[9]>2.0:
					return 'True'
				else: return 'True'
			elif obj[7]<=1:
				return 'True'
			else: return 'True'
		elif obj[6]>2:
			# {"feature": "Bar", "instances": 21, "metric_value": 0.9984, "depth": 3}
			if obj[8]>0.0:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[7]<=7:
					# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[9]<=3.0:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[4]>0:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]>1:
									# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]<=1:
										# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5]<=1:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]<=1:
													# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[12]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=1:
									return 'True'
								else: return 'True'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[9]>3.0:
						return 'False'
					else: return 'False'
				elif obj[7]>7:
					return 'False'
				else: return 'False'
			elif obj[8]<=0.0:
				# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>2:
						return 'True'
					elif obj[1]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[7]<=10:
			# {"feature": "Bar", "instances": 16, "metric_value": 0.6962, "depth": 3}
			if obj[8]>0.0:
				# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[6]<=3:
					# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[4]<=3:
						return 'False'
					elif obj[4]>3:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>0:
							return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]>3:
					return 'True'
				else: return 'True'
			elif obj[8]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[7]>10:
			return 'True'
		else: return 'True'
	else: return 'False'
