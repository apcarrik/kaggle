def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[10]<=8.313725490196079:
		# {"feature": "Coupon", "instances": 29, "metric_value": 0.8936, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Time", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[2]<=3:
				return 'True'
			elif obj[2]>3:
				# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>3:
			# {"feature": "Gender", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[5]>0:
				# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					# {"feature": "Coffeehouse", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[13]>1.0:
						return 'False'
					elif obj[13]<=1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[10]>8.313725490196079:
		# {"feature": "Income", "instances": 22, "metric_value": 0.9457, "depth": 2}
		if obj[11]>2:
			# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[14]>0.0:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[3]<=3:
					# {"feature": "Distance", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[16]>1:
						# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[5]>0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[12]<=1.0:
									return 'True'
								elif obj[12]>1.0:
									return 'False'
								else: return 'False'
							elif obj[0]>2:
								return 'False'
							else: return 'False'
						elif obj[5]<=0:
							return 'True'
						else: return 'True'
					elif obj[16]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]>3:
					return 'False'
				else: return 'False'
			elif obj[14]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[11]<=2:
			return 'False'
		else: return 'False'
	else: return 'False'
