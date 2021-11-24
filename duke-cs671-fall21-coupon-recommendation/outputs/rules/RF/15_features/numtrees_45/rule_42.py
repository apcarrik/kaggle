def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 16, "metric_value": 1.0, "depth": 2}
		if obj[8]>2:
			# {"feature": "Time", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[2]>1:
					# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[7]<=3:
						return 'True'
					elif obj[7]>3:
						return 'False'
					else: return 'False'
				elif obj[2]<=1:
					# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[10]<=1.0:
						return 'False'
					elif obj[10]>1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[8]<=2:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		return 'False'
	else: return 'False'
