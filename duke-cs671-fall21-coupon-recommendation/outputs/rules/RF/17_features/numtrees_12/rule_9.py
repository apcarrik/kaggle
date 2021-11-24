def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Income", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[11]<=7:
		# {"feature": "Age", "instances": 79, "metric_value": 0.986, "depth": 2}
		if obj[6]<=5:
			# {"feature": "Occupation", "instances": 63, "metric_value": 0.9998, "depth": 3}
			if obj[10]>2:
				# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9864, "depth": 4}
				if obj[13]<=1.0:
					# {"feature": "Passanger", "instances": 26, "metric_value": 0.8404, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Coupon", "instances": 22, "metric_value": 0.684, "depth": 6}
						if obj[3]>1:
							# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 7}
							if obj[12]>0.0:
								# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.5033, "depth": 8}
								if obj[14]<=1.0:
									return 'False'
								elif obj[14]>1.0:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[2]>0:
										return 'True'
									elif obj[2]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[12]<=0.0:
								# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[4]>0:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5]>0:
										return 'False'
									elif obj[5]<=0:
										return 'True'
									else: return 'True'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]<=1:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[9]<=1:
							return 'True'
						elif obj[9]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[13]>1.0:
					# {"feature": "Passanger", "instances": 25, "metric_value": 0.971, "depth": 5}
					if obj[0]>0:
						# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 6}
						if obj[14]>0.0:
							# {"feature": "Bar", "instances": 21, "metric_value": 0.9984, "depth": 7}
							if obj[12]<=3.0:
								# {"feature": "Distance", "instances": 20, "metric_value": 1.0, "depth": 8}
								if obj[16]>1:
									# {"feature": "Weather", "instances": 13, "metric_value": 0.9612, "depth": 9}
									if obj[1]<=0:
										# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[2]>1:
											# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[8]<=0:
												return 'True'
											elif obj[8]>0:
												return 'False'
											else: return 'False'
										elif obj[2]<=1:
											return 'False'
										else: return 'False'
									elif obj[1]>0:
										# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[2]<=1:
											return 'True'
										elif obj[2]>1:
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5]<=0:
												return 'False'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[16]<=1:
									# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[3]<=2:
										return 'False'
									elif obj[3]>2:
										# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1]<=0:
											return 'True'
										elif obj[1]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[12]>3.0:
								return 'True'
							else: return 'True'
						elif obj[14]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[10]<=2:
				# {"feature": "Weather", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[12]<=1.0:
						return 'True'
					elif obj[12]>1.0:
						return 'False'
					else: return 'False'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>5:
			# {"feature": "Education", "instances": 16, "metric_value": 0.6962, "depth": 3}
			if obj[9]>1:
				# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[10]>1:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[0]>1:
							# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[4]<=0:
								return 'True'
							elif obj[4]>0:
								return 'False'
							else: return 'False'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					elif obj[10]<=1:
						return 'True'
					else: return 'True'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			elif obj[9]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[11]>7:
		return 'False'
	else: return 'False'
