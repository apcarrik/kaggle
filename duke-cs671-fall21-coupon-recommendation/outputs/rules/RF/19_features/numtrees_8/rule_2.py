def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Distance", "instances": 127, "metric_value": 0.9838, "depth": 1}
	if obj[18]>1:
		# {"feature": "Coupon_validity", "instances": 69, "metric_value": 0.9877, "depth": 2}
		if obj[5]<=0:
			# {"feature": "Coupon", "instances": 38, "metric_value": 0.9819, "depth": 3}
			if obj[4]>1:
				# {"feature": "Time", "instances": 21, "metric_value": 0.7025, "depth": 4}
				if obj[3]<=3:
					# {"feature": "Occupation", "instances": 16, "metric_value": 0.3373, "depth": 5}
					if obj[11]<=18:
						return 'True'
					elif obj[11]>18:
						return 'False'
					else: return 'False'
				elif obj[3]>3:
					# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]>30:
						return 'False'
					elif obj[2]<=30:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=1:
				# {"feature": "Occupation", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[11]>2:
					# {"feature": "Gender", "instances": 15, "metric_value": 0.7219, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[12]>0:
								return 'True'
							elif obj[12]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[6]>0:
						return 'False'
					else: return 'False'
				elif obj[11]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]>0:
			# {"feature": "Age", "instances": 31, "metric_value": 0.8238, "depth": 3}
			if obj[7]>2:
				# {"feature": "Restaurantlessthan20", "instances": 16, "metric_value": 0.9887, "depth": 4}
				if obj[15]>1.0:
					# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[11]<=6:
						# {"feature": "Children", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[9]>0:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[0]>1:
								return 'True'
							elif obj[0]<=1:
								# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]<=55:
									return 'False'
								elif obj[2]>55:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[9]<=0:
							return 'False'
						else: return 'False'
					elif obj[11]>6:
						return 'True'
					else: return 'True'
				elif obj[15]<=1.0:
					return 'False'
				else: return 'False'
			elif obj[7]<=2:
				# {"feature": "Time", "instances": 15, "metric_value": 0.3534, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=55:
						return 'False'
					elif obj[2]>55:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[18]<=1:
		# {"feature": "Age", "instances": 58, "metric_value": 0.8247, "depth": 2}
		if obj[7]<=3:
			# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.9629, "depth": 3}
			if obj[14]<=3.0:
				# {"feature": "Gender", "instances": 28, "metric_value": 0.9059, "depth": 4}
				if obj[6]>0:
					# {"feature": "Income", "instances": 20, "metric_value": 0.7219, "depth": 5}
					if obj[12]>1:
						# {"feature": "Temperature", "instances": 14, "metric_value": 0.3712, "depth": 6}
						if obj[2]>30:
							return 'True'
						elif obj[2]<=30:
							# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=0:
								return 'False'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[12]<=1:
						# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[4]>2:
							return 'True'
						elif obj[4]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]<=0:
					# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[15]>1.0:
						# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]<=3:
							# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>30:
								return 'False'
							elif obj[2]<=30:
								return 'True'
							else: return 'True'
						elif obj[3]>3:
							return 'True'
						else: return 'True'
					elif obj[15]<=1.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[14]>3.0:
				return 'False'
			else: return 'False'
		elif obj[7]>3:
			# {"feature": "Coffeehouse", "instances": 27, "metric_value": 0.5033, "depth": 3}
			if obj[14]>1.0:
				return 'True'
			elif obj[14]<=1.0:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[4]>2:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[16]<=1.0:
						# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]<=1:
							return 'False'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[16]>1.0:
						return 'True'
					else: return 'True'
				elif obj[4]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
