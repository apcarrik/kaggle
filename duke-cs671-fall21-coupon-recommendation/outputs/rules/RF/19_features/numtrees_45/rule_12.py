def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[11]>4:
		# {"feature": "Direction_same", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[17]<=0:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Weather", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			elif obj[4]>2:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[17]>0:
			return 'True'
		else: return 'True'
	elif obj[11]<=4:
		return 'True'
	else: return 'True'
