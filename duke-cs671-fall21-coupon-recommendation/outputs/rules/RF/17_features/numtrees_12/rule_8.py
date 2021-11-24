def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Time", "instances": 58, "metric_value": 0.9444, "depth": 2}
		if obj[2]>0:
			# {"feature": "Bar", "instances": 45, "metric_value": 0.8673, "depth": 3}
			if obj[12]<=3.0:
				# {"feature": "Age", "instances": 43, "metric_value": 0.8204, "depth": 4}
				if obj[6]<=4:
					# {"feature": "Coffeehouse", "instances": 38, "metric_value": 0.868, "depth": 5}
					if obj[13]<=2.0:
						# {"feature": "Occupation", "instances": 27, "metric_value": 0.951, "depth": 6}
						if obj[10]>5:
							# {"feature": "Weather", "instances": 16, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=0:
								# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 8}
								if obj[9]>0:
									return 'False'
								elif obj[9]<=0:
									# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]<=3:
										return 'False'
									elif obj[3]>3:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]>0:
								# {"feature": "Coupon_validity", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[4]<=0:
									# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]>0:
										return 'True'
									elif obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[4]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[10]<=5:
							# {"feature": "Weather", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[1]<=0:
								# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[5]>0:
									return 'True'
								elif obj[5]<=0:
									# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[11]>2:
										return 'False'
									elif obj[11]<=2:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[13]>2.0:
						# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 6}
						if obj[10]<=20:
							return 'False'
						elif obj[10]>20:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]>4:
					return 'False'
				else: return 'False'
			elif obj[12]>3.0:
				return 'True'
			else: return 'True'
		elif obj[2]<=0:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[14]>0.0:
				# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[6]<=6:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[12]<=1.0:
						return 'True'
					elif obj[12]>1.0:
						# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>6:
					return 'False'
				else: return 'False'
			elif obj[14]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Occupation", "instances": 27, "metric_value": 0.9183, "depth": 2}
		if obj[10]>4:
			# {"feature": "Maritalstatus", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[7]<=2:
				# {"feature": "Income", "instances": 15, "metric_value": 0.3534, "depth": 4}
				if obj[11]>0:
					return 'True'
				elif obj[11]<=0:
					return 'False'
				else: return 'False'
			elif obj[7]>2:
				return 'False'
			else: return 'False'
		elif obj[10]<=4:
			# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[9]<=1:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[3]>0:
					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]>0:
							return 'True'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[9]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
