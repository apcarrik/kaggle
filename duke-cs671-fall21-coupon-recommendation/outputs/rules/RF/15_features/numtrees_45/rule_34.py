def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[9]>2:
		# {"feature": "Children", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Coupon_validity", "instances": 12, "metric_value": 1.0, "depth": 3}
			if obj[3]>0:
				# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[5]<=4:
					return 'False'
				elif obj[5]>4:
					return 'True'
				else: return 'True'
			elif obj[3]<=0:
				# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[11]>0.0:
					return 'True'
				elif obj[11]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>0:
			return 'False'
		else: return 'False'
	elif obj[9]<=2:
		return 'True'
	else: return 'True'
