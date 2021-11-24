def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9831, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Coffeehouse", "instances": 54, "metric_value": 0.9183, "depth": 2}
		if obj[10]<=2.0:
			# {"feature": "Age", "instances": 42, "metric_value": 0.7919, "depth": 3}
			if obj[4]>1:
				# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.9306, "depth": 4}
				if obj[11]<=1.0:
					# {"feature": "Direction_same", "instances": 21, "metric_value": 0.9852, "depth": 5}
					if obj[12]<=0:
						# {"feature": "Passanger", "instances": 17, "metric_value": 0.9975, "depth": 6}
						if obj[0]>0:
							# {"feature": "Occupation", "instances": 15, "metric_value": 0.9968, "depth": 7}
							if obj[7]<=16:
								# {"feature": "Income", "instances": 13, "metric_value": 0.9612, "depth": 8}
								if obj[8]>0:
									# {"feature": "Gender", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[3]>0:
										# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[6]>1:
											# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[1]>0:
												# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[9]>0.0:
													return 'True'
												elif obj[9]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[1]<=0:
												return 'True'
											else: return 'True'
										elif obj[6]<=1:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[9]<=2.0:
											return 'True'
										elif obj[9]>2.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[8]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]>16:
								return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[12]>0:
						return 'True'
					else: return 'True'
				elif obj[11]>1.0:
					return 'True'
				else: return 'True'
			elif obj[4]<=1:
				# {"feature": "Children", "instances": 16, "metric_value": 0.3373, "depth": 4}
				if obj[5]<=0:
					return 'True'
				elif obj[5]>0:
					# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]<=5:
						return 'True'
					elif obj[7]>5:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[10]>2.0:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[7]>5:
				# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[4]<=4:
					return 'False'
				elif obj[4]>4:
					return 'True'
				else: return 'True'
			elif obj[7]<=5:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>3:
		# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[10]<=1.0:
			# {"feature": "Age", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[4]<=2:
				return 'False'
			elif obj[4]>2:
				# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Bar", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[9]<=0.0:
						return 'False'
					elif obj[9]>0.0:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]<=0:
							return 'False'
						elif obj[6]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]>1.0:
			# {"feature": "Time", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[1]>1:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[11]>0.0:
					return 'True'
				elif obj[11]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[9]>0.0:
					return 'False'
				elif obj[9]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'False'
