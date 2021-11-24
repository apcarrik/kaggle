def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Income", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[13]<=5:
		# {"feature": "Education", "instances": 56, "metric_value": 0.9403, "depth": 2}
		if obj[11]>1:
			# {"feature": "Restaurantlessthan20", "instances": 33, "metric_value": 0.7455, "depth": 3}
			if obj[16]>0.0:
				# {"feature": "Bar", "instances": 31, "metric_value": 0.6374, "depth": 4}
				if obj[14]<=1.0:
					# {"feature": "Maritalstatus", "instances": 20, "metric_value": 0.8113, "depth": 5}
					if obj[9]<=1:
						# {"feature": "Gender", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[7]>0:
							# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 7}
							if obj[4]>0:
								# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[6]>0:
									return 'False'
								elif obj[6]<=0:
									# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5]>0:
										return 'True'
									elif obj[5]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						elif obj[7]<=0:
							return 'False'
						else: return 'False'
					elif obj[9]>1:
						return 'False'
					else: return 'False'
				elif obj[14]>1.0:
					return 'False'
				else: return 'False'
			elif obj[16]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[11]<=1:
			# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Coupon", "instances": 18, "metric_value": 0.9911, "depth": 4}
				if obj[5]<=3:
					# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[15]<=1.0:
						# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[4]<=2:
							# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[8]>0:
								# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]>1:
									# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6]>0:
										return 'False'
									elif obj[6]<=0:
										return 'True'
									else: return 'True'
								elif obj[0]<=1:
									return 'False'
								else: return 'False'
							elif obj[8]<=0:
								return 'True'
							else: return 'True'
						elif obj[4]>2:
							return 'False'
						else: return 'False'
					elif obj[15]>1.0:
						return 'True'
					else: return 'True'
				elif obj[5]>3:
					# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[2]<=0:
						return 'False'
					elif obj[2]>0:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=0:
							return 'True'
						elif obj[4]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[13]>5:
		# {"feature": "Bar", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[14]<=3.0:
			# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.8767, "depth": 3}
			if obj[17]<=1.0:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[12]<=10:
					# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[18]<=0:
						# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[15]<=3.0:
							return 'False'
						elif obj[15]>3.0:
							# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=0:
								return 'True'
							elif obj[0]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[18]>0:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[8]>1:
							return 'True'
						elif obj[8]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[12]>10:
					return 'True'
				else: return 'True'
			elif obj[17]>1.0:
				# {"feature": "Weather", "instances": 12, "metric_value": 0.4138, "depth": 4}
				if obj[2]<=1:
					return 'True'
				elif obj[2]>1:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>2:
						return 'True'
					elif obj[4]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[14]>3.0:
			return 'False'
		else: return 'False'
	else: return 'True'
