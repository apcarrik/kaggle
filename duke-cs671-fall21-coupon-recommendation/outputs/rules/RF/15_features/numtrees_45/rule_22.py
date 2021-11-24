def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Time", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Income", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[9]>0:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[12]>0.0:
					return 'False'
				elif obj[12]<=0.0:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]<=3:
						return 'True'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]<=0:
				# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[6]<=0:
					return 'True'
				elif obj[6]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>1:
			# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[5]<=4:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[14]<=2:
					return 'True'
				elif obj[14]>2:
					return 'False'
				else: return 'False'
			elif obj[5]>4:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
