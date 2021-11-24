def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[7]<=3:
		# {"feature": "Time", "instances": 35, "metric_value": 0.9947, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.9306, "depth": 3}
			if obj[16]>0.0:
				# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.8281, "depth": 4}
				if obj[14]<=1.0:
					# {"feature": "Bar", "instances": 12, "metric_value": 0.4138, "depth": 5}
					if obj[13]<=1.0:
						return 'False'
					elif obj[13]>1.0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[14]>1.0:
					# {"feature": "Restaurantlessthan20", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[15]>2.0:
						# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[13]<=2.0:
							return 'False'
						elif obj[13]>2.0:
							return 'True'
						else: return 'True'
					elif obj[15]<=2.0:
						# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[9]>0:
							return 'True'
						elif obj[9]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[16]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[3]>3:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[11]<=12:
				return 'True'
			elif obj[11]>12:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[7]>3:
		# {"feature": "Coupon_validity", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[5]<=0:
			return 'True'
		elif obj[5]>0:
			# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]<=1:
					return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[3]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
