def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[2]>1:
			# {"feature": "Bar", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[8]<=2.0:
				return 'False'
			elif obj[8]>2.0:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[9]>1.0:
			return 'True'
		elif obj[9]<=1.0:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=0:
					return 'True'
				elif obj[5]>0:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
