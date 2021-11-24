def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[4]>1:
		# {"feature": "Education", "instances": 64, "metric_value": 0.9422, "depth": 2}
		if obj[10]<=3:
			# {"feature": "Occupation", "instances": 56, "metric_value": 0.9769, "depth": 3}
			if obj[11]<=19:
				# {"feature": "Gender", "instances": 52, "metric_value": 0.9471, "depth": 4}
				if obj[6]>0:
					# {"feature": "Passanger", "instances": 28, "metric_value": 0.7496, "depth": 5}
					if obj[0]>1:
						# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.3534, "depth": 6}
						if obj[14]<=2.0:
							return 'True'
						elif obj[14]>2.0:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]>3:
								return 'False'
							elif obj[3]<=3:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[0]<=1:
						# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.9612, "depth": 6}
						if obj[14]>1.0:
							# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[3]>0:
								return 'True'
							elif obj[3]<=0:
								return 'False'
							else: return 'False'
						elif obj[14]<=1.0:
							# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[9]<=0:
									return 'True'
								elif obj[9]>0:
									return 'False'
								else: return 'False'
							elif obj[3]>0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]<=0:
					# {"feature": "Age", "instances": 24, "metric_value": 0.995, "depth": 5}
					if obj[7]>2:
						# {"feature": "Distance", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[18]>1:
							# {"feature": "Time", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[3]<=3:
								# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[13]<=2.0:
									# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1]<=0:
											# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5]>0:
												return 'True'
											elif obj[5]<=0:
												return 'False'
											else: return 'False'
										elif obj[1]>0:
											return 'False'
										else: return 'False'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								elif obj[13]>2.0:
									return 'True'
								else: return 'True'
							elif obj[3]>3:
								return 'True'
							else: return 'True'
						elif obj[18]<=1:
							return 'True'
						else: return 'True'
					elif obj[7]<=2:
						# {"feature": "Coupon_validity", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[5]>0:
							return 'False'
						elif obj[5]<=0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>2:
								return 'True'
							elif obj[0]<=2:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[11]>19:
				return 'False'
			else: return 'False'
		elif obj[10]>3:
			return 'True'
		else: return 'True'
	elif obj[4]<=1:
		# {"feature": "Occupation", "instances": 21, "metric_value": 0.9183, "depth": 2}
		if obj[11]<=12:
			# {"feature": "Temperature", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[2]<=55:
				return 'False'
			elif obj[2]>55:
				# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[8]>0:
					return 'False'
				elif obj[8]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[11]>12:
			# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[13]<=2.0:
				return 'True'
			elif obj[13]>2.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
