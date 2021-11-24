def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[13]>0.0:
		# {"feature": "Children", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[7]<=0:
			# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[15]<=2:
				return 'True'
			elif obj[15]>2:
				return 'False'
			else: return 'False'
		elif obj[7]>0:
			# {"feature": "Coupon_validity", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[4]>0:
				# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[5]>0:
					return 'True'
				elif obj[5]<=0:
					return 'False'
				else: return 'False'
			elif obj[4]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[13]<=0.0:
		return 'False'
	else: return 'False'
