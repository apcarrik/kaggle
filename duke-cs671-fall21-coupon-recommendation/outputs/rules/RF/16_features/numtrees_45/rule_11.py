def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[10]<=5:
		# {"feature": "Distance", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[15]<=2:
			# {"feature": "Passanger", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[0]>0:
				# {"feature": "Occupation", "instances": 14, "metric_value": 0.3712, "depth": 4}
				if obj[9]>2:
					return 'True'
				elif obj[9]<=2:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=3:
						return 'True'
					elif obj[3]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[15]>2:
			return 'False'
		else: return 'False'
	elif obj[10]>5:
		return 'False'
	else: return 'False'
