def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Bar", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[10]<=2.0:
		# {"feature": "Coupon", "instances": 76, "metric_value": 1.0, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Restaurant20to50", "instances": 56, "metric_value": 0.9769, "depth": 3}
			if obj[12]>0.0:
				# {"feature": "Coffeehouse", "instances": 46, "metric_value": 0.9986, "depth": 4}
				if obj[11]<=2.0:
					# {"feature": "Direction_same", "instances": 34, "metric_value": 0.9597, "depth": 5}
					if obj[13]<=0:
						# {"feature": "Occupation", "instances": 25, "metric_value": 0.9988, "depth": 6}
						if obj[8]<=12:
							# {"feature": "Income", "instances": 21, "metric_value": 0.9852, "depth": 7}
							if obj[9]>3:
								# {"feature": "Time", "instances": 11, "metric_value": 0.9457, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 10}
										if obj[5]<=2:
											# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[3]<=0:
												return 'True'
											elif obj[3]>0:
												# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[14]<=1:
													return 'False'
												elif obj[14]>1:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[5]>2:
											return 'False'
										else: return 'False'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								elif obj[1]>3:
									return 'False'
								else: return 'False'
							elif obj[9]<=3:
								# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[1]>0:
										# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[0]>0:
											return 'False'
										elif obj[0]<=0:
											# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								elif obj[7]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[8]>12:
							return 'True'
						else: return 'True'
					elif obj[13]>0:
						# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[8]<=19:
							return 'True'
						elif obj[8]>19:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[11]>2.0:
					# {"feature": "Occupation", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[8]>6:
						# {"feature": "Income", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[9]>4:
							# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[14]>1:
								return 'False'
							elif obj[14]<=1:
								return 'True'
							else: return 'True'
						elif obj[9]<=4:
							return 'True'
						else: return 'True'
					elif obj[8]<=6:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[12]<=0.0:
				# {"feature": "Time", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[2]>3:
			# {"feature": "Income", "instances": 20, "metric_value": 0.8113, "depth": 3}
			if obj[9]<=6:
				# {"feature": "Coupon_validity", "instances": 18, "metric_value": 0.65, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					# {"feature": "Coffeehouse", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[11]>0.0:
						# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[8]<=15:
							return 'True'
						elif obj[8]>15:
							return 'False'
						else: return 'False'
					elif obj[11]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]>6:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[10]>2.0:
		# {"feature": "Direction_same", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[13]<=0:
			return 'True'
		elif obj[13]>0:
			# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
