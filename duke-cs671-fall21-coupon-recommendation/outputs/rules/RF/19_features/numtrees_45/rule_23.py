def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[4]>1:
		# {"feature": "Coupon_validity", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[5]<=0:
			return 'True'
		elif obj[5]>0:
			# {"feature": "Temperature", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[2]>55:
				# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]>3:
					# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]<=0:
						return 'True'
					elif obj[6]>0:
						return 'False'
					else: return 'False'
				elif obj[3]<=3:
					return 'False'
				else: return 'False'
			elif obj[2]<=55:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]<=1:
		# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[10]<=2:
			return 'False'
		elif obj[10]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
