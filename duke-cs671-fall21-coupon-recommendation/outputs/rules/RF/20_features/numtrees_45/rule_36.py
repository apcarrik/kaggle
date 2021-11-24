def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[12]<=10:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[5]<=3:
				# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[6]<=0:
					return 'True'
				elif obj[6]>0:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[8]>1:
						return 'False'
					elif obj[8]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>3:
				# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[10]<=0:
					return 'False'
				elif obj[10]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[12]>10:
			return 'False'
		else: return 'False'
	elif obj[1]>1:
		return 'True'
	else: return 'True'
