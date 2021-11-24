def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.971, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 61, "metric_value": 0.8949, "depth": 2}
		if obj[7]>0:
			# {"feature": "Age", "instances": 59, "metric_value": 0.8663, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Time", "instances": 30, "metric_value": 0.971, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Income", "instances": 26, "metric_value": 0.9957, "depth": 5}
					if obj[8]>2:
						# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9587, "depth": 6}
						if obj[11]>0.0:
							# {"feature": "Distance", "instances": 19, "metric_value": 0.9819, "depth": 7}
							if obj[13]>1:
								# {"feature": "Education", "instances": 13, "metric_value": 0.8905, "depth": 8}
								if obj[6]<=3:
									# {"feature": "Gender", "instances": 12, "metric_value": 0.8113, "depth": 9}
									if obj[3]>0:
										# {"feature": "Bar", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[9]>1.0:
											return 'True'
										elif obj[9]<=1.0:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[0]>1:
												return 'True'
											elif obj[0]<=1:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[9]<=1.0:
												return 'True'
											elif obj[9]>1.0:
												return 'False'
											else: return 'False'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[6]>3:
									return 'False'
								else: return 'False'
							elif obj[13]<=1:
								# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[6]>0:
										return 'False'
									elif obj[6]<=0:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[10]>0.0:
											return 'True'
										elif obj[10]<=0.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[5]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[11]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[8]<=2:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[4]>2:
				# {"feature": "Education", "instances": 29, "metric_value": 0.6632, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Bar", "instances": 26, "metric_value": 0.5159, "depth": 5}
					if obj[9]<=1.0:
						return 'True'
					elif obj[9]>1.0:
						# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[11]>0.0:
							# {"feature": "Income", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[8]<=7:
								return 'True'
							elif obj[8]>7:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=0:
									return 'True'
								elif obj[1]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[11]<=0.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>2:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[7]<=0:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 24, "metric_value": 0.9544, "depth": 2}
		if obj[9]>0.0:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[7]<=5:
				# {"feature": "Children", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[5]>0:
					return 'True'
				elif obj[5]<=0:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=4:
						return 'False'
					elif obj[4]>4:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]>5:
				return 'False'
			else: return 'False'
		elif obj[9]<=0.0:
			# {"feature": "Time", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
