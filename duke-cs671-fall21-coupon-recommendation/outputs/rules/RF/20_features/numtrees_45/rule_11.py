def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[8]<=2:
		# {"feature": "Temperature", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[3]>55:
			return 'False'
		elif obj[3]<=55:
			# {"feature": "Driving_to", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[5]>0:
					return 'True'
				elif obj[5]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[8]>2:
		# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[5]>0:
			return 'True'
		elif obj[5]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
