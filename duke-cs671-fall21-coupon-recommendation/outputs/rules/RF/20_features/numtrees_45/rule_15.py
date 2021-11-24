def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Weather", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[2]<=0:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.7425, "depth": 2}
		if obj[12]<=19:
			# {"feature": "Temperature", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[3]>30:
				return 'True'
			elif obj[3]<=30:
				# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[8]<=1:
					return 'False'
				elif obj[8]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[12]>19:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[5]<=2:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[8]<=1:
					return 'True'
				elif obj[8]>1:
					return 'False'
				else: return 'False'
			elif obj[5]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]>0:
		return 'False'
	else: return 'False'
