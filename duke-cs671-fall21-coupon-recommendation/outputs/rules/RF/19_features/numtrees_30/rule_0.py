def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[10]<=3:
		# {"feature": "Bar", "instances": 28, "metric_value": 0.9963, "depth": 2}
		if obj[13]<=1.0:
			# {"feature": "Distance", "instances": 20, "metric_value": 0.971, "depth": 3}
			if obj[18]<=2:
				# {"feature": "Weather", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Time", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[11]<=19:
							return 'False'
						elif obj[11]>19:
							# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]>2:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[11]<=12:
							return 'True'
						elif obj[11]>12:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			elif obj[18]>2:
				return 'False'
			else: return 'False'
		elif obj[13]>1.0:
			# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[16]>0.0:
				return 'True'
			elif obj[16]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[10]>3:
		return 'True'
	else: return 'True'
