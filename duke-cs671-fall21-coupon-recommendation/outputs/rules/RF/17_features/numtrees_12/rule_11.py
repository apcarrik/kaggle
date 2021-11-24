def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9555, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon", "instances": 68, "metric_value": 0.9944, "depth": 2}
		if obj[3]>1:
			# {"feature": "Coffeehouse", "instances": 46, "metric_value": 0.9109, "depth": 3}
			if obj[13]<=1.0:
				# {"feature": "Weather", "instances": 24, "metric_value": 1.0, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Income", "instances": 21, "metric_value": 0.9852, "depth": 5}
					if obj[11]>2:
						# {"feature": "Time", "instances": 16, "metric_value": 0.9887, "depth": 6}
						if obj[2]>0:
							# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[10]<=12:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[15]<=0:
									return 'True'
								elif obj[15]>0:
									# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4]<=0:
										return 'True'
									elif obj[4]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[10]>12:
								return 'False'
							else: return 'False'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[11]<=2:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[13]>1.0:
				# {"feature": "Direction_same", "instances": 22, "metric_value": 0.5746, "depth": 4}
				if obj[15]<=0:
					return 'True'
				elif obj[15]>0:
					# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[4]<=0:
						return 'True'
					elif obj[4]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[3]<=1:
			# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.8454, "depth": 3}
			if obj[14]<=2.0:
				# {"feature": "Maritalstatus", "instances": 20, "metric_value": 0.7219, "depth": 4}
				if obj[7]<=0:
					# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[12]<=0.0:
						# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[2]<=1:
							return 'False'
						elif obj[2]>1:
							# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[12]>0.0:
						# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=0:
							return 'True'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[7]>0:
					return 'False'
				else: return 'False'
			elif obj[14]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.3228, "depth": 2}
		if obj[10]<=11:
			return 'True'
		elif obj[10]>11:
			return 'False'
		else: return 'False'
	else: return 'True'
