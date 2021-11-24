def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Income", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[12]>2:
		# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.6962, "depth": 2}
		if obj[16]<=1.0:
			# {"feature": "Maritalstatus", "instances": 20, "metric_value": 0.8813, "depth": 3}
			if obj[8]>0:
				# {"feature": "Time", "instances": 12, "metric_value": 0.4138, "depth": 4}
				if obj[3]<=3:
					return 'True'
				elif obj[3]>3:
					return 'False'
				else: return 'False'
			elif obj[8]<=0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[11]>5:
					# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3]<=3:
						return 'False'
					elif obj[3]>3:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>2:
							return 'False'
						elif obj[0]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[11]<=5:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[16]>1.0:
			return 'True'
		else: return 'True'
	elif obj[12]<=2:
		# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[14]>1.0:
			# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[10]<=3:
				# {"feature": "Weather", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[3]<=2:
						return 'True'
					elif obj[3]>2:
						return 'False'
					else: return 'False'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			elif obj[10]>3:
				return 'False'
			else: return 'False'
		elif obj[14]<=1.0:
			return 'False'
		else: return 'False'
	else: return 'False'
