def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[13]<=2.0:
		# {"feature": "Distance", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[15]>1:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[9]>2:
				return 'False'
			elif obj[9]<=2:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>2:
					return 'False'
				elif obj[0]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[15]<=1:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[3]>2:
				return 'True'
			elif obj[3]<=2:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[13]>2.0:
		return 'True'
	else: return 'True'
