def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[8]>4:
		# {"feature": "Bar", "instances": 20, "metric_value": 0.8113, "depth": 2}
		if obj[10]>0.0:
			# {"feature": "Passanger", "instances": 15, "metric_value": 0.3534, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]>1:
					return 'False'
				elif obj[5]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]<=0.0:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[8]<=4:
		return 'True'
	else: return 'True'
