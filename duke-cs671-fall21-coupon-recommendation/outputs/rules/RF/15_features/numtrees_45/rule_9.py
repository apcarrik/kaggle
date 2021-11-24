def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Education", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[7]<=3:
			# {"feature": "Age", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[5]<=2:
				return 'False'
			elif obj[5]>2:
				# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[3]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[7]>3:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[8]<=12:
			return 'True'
		elif obj[8]>12:
			# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]>3:
				return 'True'
			elif obj[1]<=3:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
