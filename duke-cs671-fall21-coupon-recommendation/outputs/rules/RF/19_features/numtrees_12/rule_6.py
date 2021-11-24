def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon_validity", "instances": 85, "metric_value": 0.9991, "depth": 1}
	if obj[5]>0:
		# {"feature": "Time", "instances": 44, "metric_value": 0.976, "depth": 2}
		if obj[3]<=1:
			# {"feature": "Restaurantlessthan20", "instances": 26, "metric_value": 0.8404, "depth": 3}
			if obj[15]<=2.0:
				# {"feature": "Coupon", "instances": 16, "metric_value": 0.9887, "depth": 4}
				if obj[4]<=3:
					# {"feature": "Age", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[7]>0:
						# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[14]>1.0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]>30:
									return 'False'
								elif obj[2]<=30:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[14]<=1.0:
							return 'True'
						else: return 'True'
					elif obj[7]<=0:
						return 'False'
					else: return 'False'
				elif obj[4]>3:
					# {"feature": "Temperature", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[2]>55:
						return 'False'
					elif obj[2]<=55:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[15]>2.0:
				return 'False'
			else: return 'False'
		elif obj[3]>1:
			# {"feature": "Coupon", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[4]>0:
				# {"feature": "Education", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[10]>1:
					# {"feature": "Coffeehouse", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[14]<=2.0:
						# {"feature": "Temperature", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=55:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]>55:
							return 'True'
						else: return 'True'
					elif obj[14]>2.0:
						return 'False'
					else: return 'False'
				elif obj[10]<=1:
					# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[0]>0:
						return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[5]<=0:
		# {"feature": "Occupation", "instances": 41, "metric_value": 0.9474, "depth": 2}
		if obj[11]<=9:
			# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.7219, "depth": 3}
			if obj[16]>-1.0:
				# {"feature": "Maritalstatus", "instances": 28, "metric_value": 0.5917, "depth": 4}
				if obj[8]<=1:
					# {"feature": "Restaurantlessthan20", "instances": 24, "metric_value": 0.4138, "depth": 5}
					if obj[15]>1.0:
						return 'True'
					elif obj[15]<=1.0:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]<=3:
							return 'True'
						elif obj[4]>3:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[8]>1:
					# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[16]<=-1.0:
				return 'False'
			else: return 'False'
		elif obj[11]>9:
			# {"feature": "Bar", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[13]<=1.0:
				return 'False'
			elif obj[13]>1.0:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'True'
