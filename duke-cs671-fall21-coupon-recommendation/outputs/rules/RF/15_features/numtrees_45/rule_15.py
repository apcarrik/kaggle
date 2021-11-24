def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[8]<=8:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[2]>1:
			# {"feature": "Age", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[5]>0:
				# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[7]<=2:
					return 'True'
				elif obj[7]>2:
					return 'False'
				else: return 'False'
			elif obj[5]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	elif obj[8]>8:
		return 'False'
	else: return 'False'
