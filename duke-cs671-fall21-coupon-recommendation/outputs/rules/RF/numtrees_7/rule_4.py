def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Driving_to", "instances": 146, "metric_value": 0.9951, "depth": 1}
	if obj[0]<=0:
		# {"feature": "Occupation", "instances": 80, "metric_value": 0.896, "depth": 2}
		if obj[12]<=8.0375:
			# {"feature": "Coffeehouse", "instances": 50, "metric_value": 0.5294, "depth": 3}
			if obj[15]>-1.0:
				# {"feature": "Children", "instances": 49, "metric_value": 0.4754, "depth": 4}
				if obj[10]<=0:
					# {"feature": "Coupon", "instances": 30, "metric_value": 0.2108, "depth": 5}
					if obj[5]<=3:
						return 'True'
					elif obj[5]>3:
						# {"feature": "Carryaway", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[16]>2.0:
							return 'True'
						elif obj[16]<=2.0:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[8]<=2:
								return 'True'
							elif obj[8]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[10]>0:
					# {"feature": "Coupon", "instances": 19, "metric_value": 0.7425, "depth": 5}
					if obj[5]>0:
						# {"feature": "Carryaway", "instances": 18, "metric_value": 0.65, "depth": 6}
						if obj[16]<=2.0:
							return 'True'
						elif obj[16]>2.0:
							# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[11]>0:
								# {"feature": "Income", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[13]<=4:
									# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[17]<=3.0:
										return 'True'
									elif obj[17]>3.0:
										return 'False'
									else: return 'False'
								elif obj[13]>4:
									return 'False'
								else: return 'False'
							elif obj[11]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[15]<=-1.0:
				return 'False'
			else: return 'False'
		elif obj[12]>8.0375:
			# {"feature": "Weather", "instances": 30, "metric_value": 0.9481, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Distance", "instances": 26, "metric_value": 0.9829, "depth": 4}
				if obj[20]>1:
					# {"feature": "Coupon", "instances": 15, "metric_value": 0.8366, "depth": 5}
					if obj[5]>1:
						# {"feature": "Age", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[8]>1:
							return 'False'
						elif obj[8]<=1:
							# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[15]<=1.0:
								# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=0:
									return 'True'
								elif obj[7]>0:
									return 'False'
								else: return 'False'
							elif obj[15]>1.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[5]<=1:
						return 'True'
					else: return 'True'
				elif obj[20]<=1:
					# {"feature": "Age", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[8]>0:
						# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[14]<=1.0:
							return 'True'
						elif obj[14]>1.0:
							# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]>55:
								return 'False'
							elif obj[3]<=55:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[8]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>0:
		# {"feature": "Income", "instances": 66, "metric_value": 0.9457, "depth": 2}
		if obj[13]<=4:
			# {"feature": "Restaurant20to50", "instances": 42, "metric_value": 0.8296, "depth": 3}
			if obj[18]<=2.0:
				# {"feature": "Age", "instances": 40, "metric_value": 0.7692, "depth": 4}
				if obj[8]<=4:
					# {"feature": "Occupation", "instances": 30, "metric_value": 0.5665, "depth": 5}
					if obj[12]<=12:
						# {"feature": "Restaurantlessthan20", "instances": 23, "metric_value": 0.258, "depth": 6}
						if obj[17]>1.0:
							return 'False'
						elif obj[17]<=1.0:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]>0:
								return 'False'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[12]>12:
						# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[11]>2:
							# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[9]<=1:
								return 'True'
							elif obj[9]>1:
								return 'False'
							else: return 'False'
						elif obj[11]<=2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[8]>4:
					# {"feature": "Gender", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[7]>0:
						# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[10]>0:
							return 'False'
						elif obj[10]<=0:
							# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]<=55:
								return 'False'
							elif obj[3]>55:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[18]>2.0:
				return 'True'
			else: return 'True'
		elif obj[13]>4:
			# {"feature": "Passanger", "instances": 24, "metric_value": 0.995, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Coupon", "instances": 22, "metric_value": 0.976, "depth": 4}
				if obj[5]<=3:
					# {"feature": "Time", "instances": 17, "metric_value": 0.874, "depth": 5}
					if obj[4]>0:
						# {"feature": "Education", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[11]>1:
							# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[15]<=2.0:
								return 'True'
							elif obj[15]>2.0:
								# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]<=0:
									return 'False'
								elif obj[2]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[11]<=1:
							# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[7]>0:
								return 'False'
							elif obj[7]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				elif obj[5]>3:
					# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[6]>0:
						return 'False'
					elif obj[6]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
