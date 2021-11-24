def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Maritalstatus", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[7]>0:
		# {"feature": "Income", "instances": 26, "metric_value": 0.9306, "depth": 2}
		if obj[11]>2:
			# {"feature": "Distance", "instances": 23, "metric_value": 0.8281, "depth": 3}
			if obj[17]<=1:
				# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.9852, "depth": 4}
				if obj[13]<=1.0:
					# {"feature": "Restaurantlessthan20", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[14]<=2.0:
						# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[10]<=14:
							return 'False'
						elif obj[10]>14:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>0:
								return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[14]>2.0:
						return 'True'
					else: return 'True'
				elif obj[13]>1.0:
					return 'True'
				else: return 'True'
			elif obj[17]>1:
				return 'False'
			else: return 'False'
		elif obj[11]<=2:
			return 'True'
		else: return 'True'
	elif obj[7]<=0:
		# {"feature": "Direction_same", "instances": 25, "metric_value": 0.8555, "depth": 2}
		if obj[16]<=0:
			# {"feature": "Occupation", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[10]<=12:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[3]>2:
					# {"feature": "Income", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[11]>2:
						# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[13]>0.0:
							return 'True'
						elif obj[13]<=0.0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[11]<=2:
						return 'False'
					else: return 'False'
				elif obj[3]<=2:
					return 'True'
				else: return 'True'
			elif obj[10]>12:
				return 'False'
			else: return 'False'
		elif obj[16]>0:
			return 'True'
		else: return 'True'
	else: return 'True'
