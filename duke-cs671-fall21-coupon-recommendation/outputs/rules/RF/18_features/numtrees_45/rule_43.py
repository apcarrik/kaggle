def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[13]>0.0:
		# {"feature": "Passanger", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Income", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[11]<=3:
				# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			elif obj[11]>3:
				# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[7]>1:
					return 'True'
				elif obj[7]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[13]<=0.0:
		return 'False'
	else: return 'False'
