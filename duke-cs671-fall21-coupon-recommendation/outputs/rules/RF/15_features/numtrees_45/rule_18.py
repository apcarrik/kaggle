def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[9]<=4:
		# {"feature": "Passanger", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Coupon_validity", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[3]<=0:
				# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[7]<=2:
					# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[10]<=2.0:
						return 'True'
					elif obj[10]>2.0:
						return 'False'
					else: return 'False'
				elif obj[7]>2:
					return 'False'
				else: return 'False'
			elif obj[3]>0:
				return 'False'
			else: return 'False'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[9]>4:
		return 'True'
	else: return 'True'
