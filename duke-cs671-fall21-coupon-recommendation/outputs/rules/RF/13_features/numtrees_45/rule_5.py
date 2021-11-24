def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[8]>0.0:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[2]>2:
			return 'True'
		elif obj[2]<=2:
			# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[7]<=7:
				return 'True'
			elif obj[7]>7:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[8]<=0.0:
		# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[9]<=1.0:
			return 'False'
		elif obj[9]>1.0:
			# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[0]>0:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
