def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[16]<=1.0:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.7706, "depth": 2}
		if obj[11]<=19:
			# {"feature": "Coffeehouse", "instances": 29, "metric_value": 0.6632, "depth": 3}
			if obj[14]>0.0:
				# {"feature": "Passanger", "instances": 19, "metric_value": 0.2975, "depth": 4}
				if obj[0]<=2:
					return 'True'
				elif obj[0]>2:
					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[3]<=3:
						return 'True'
					elif obj[3]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[14]<=0.0:
				# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[13]<=0.0:
					# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]>55:
						return 'False'
					elif obj[2]<=55:
						# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=0:
							return 'True'
						elif obj[1]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[13]>0.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[11]>19:
			return 'False'
		else: return 'False'
	elif obj[16]>1.0:
		# {"feature": "Bar", "instances": 20, "metric_value": 0.8113, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Age", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[7]>0:
				# {"feature": "Restaurantlessthan20", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[15]<=3.0:
					# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=0:
							return 'False'
						elif obj[6]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[15]>3.0:
					# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]<=0:
				return 'True'
			else: return 'True'
		elif obj[13]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'False'
